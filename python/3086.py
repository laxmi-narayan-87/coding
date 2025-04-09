class SecureFileSystem:
    def _init_(self):
        self.users = set()
        self.file_system = {}
        self.audit_log = []

    def add_user(self, username):
        self.users.add(username)

    def log_action(self, username, operation, target, result):
        self.audit_log.append((username, operation, target, result))
        print(result)

    def has_permission(self, username, permissions, required):
        return required in permissions.get(username, [])

    def parse_permissions(self, permissions):
        perm_dict = {}
        for perm in permissions.split(";"):
            user, perms = perm.split(":")
            perm_dict[user] = perms.split(",")
        return perm_dict

    def create_dir(self, username, path, permissions):
        if path in self.file_system:
            self.log_action(username, "CREATE_DIR", path, "DENY")
            return

        parent = "/".join(path.rstrip("/").split("/")[:-1])
        if parent and (parent not in self.file_system or not self.has_permission(username, self.file_system[parent]['permissions'], 'W')):
            self.log_action(username, "CREATE_DIR", path, "DENY")
            return

        self.file_system[path] = {
            "type": "directory",
            "owner": username,
            "permissions": self.parse_permissions(permissions),
            "contents": set()
        }
        if parent:
            self.file_system[parent]["contents"].add(path)
        self.log_action(username, "CREATE_DIR", path, "SUCCESS")

    def create_file(self, username, path, permissions):
        if path in self.file_system:
            self.log_action(username, "CREATE_FILE", path, "DENY")
            return

        parent = "/".join(path.split("/")[:-1])
        if not parent or parent not in self.file_system or not self.has_permission(username, self.file_system[parent]['permissions'], 'W'):
            self.log_action(username, "CREATE_FILE", path, "DENY")
            return

        self.file_system[path] = {
            "type": "file",
            "owner": username,
            "permissions": self.parse_permissions(permissions),
            "contents": ""
        }
        self.file_system[parent]["contents"].add(path)
        self.log_action(username, "CREATE_FILE", path, "SUCCESS")

    def read_file(self, username, path):
        if path not in self.file_system or self.file_system[path]["type"] != "file":
            self.log_action(username, "READ_FILE", path, "DENY")
            return

        if self.has_permission(username, self.file_system[path]["permissions"], "R"):
            self.log_action(username, "READ_FILE", path, "SUCCESS")
        else:
            self.log_action(username, "READ_FILE", path, "DENY")

    def write_file(self, username, path):
        if path not in self.file_system or self.file_system[path]["type"] != "file":
            self.log_action(username, "WRITE_FILE", path, "DENY")
            return

        if self.has_permission(username, self.file_system[path]["permissions"], "W"):
            self.log_action(username, "WRITE_FILE", path, "SUCCESS")
        else:
            self.log_action(username, "WRITE_FILE", path, "DENY")

    def list_dir(self, username, path):
        if path not in self.file_system or self.file_system[path]["type"] != "directory":
            self.log_action(username, "LIST_DIR", path, "DENY")
            return

        if self.has_permission(username, self.file_system[path]["permissions"], "R"):
            self.log_action(username, "LIST_DIR", path, "SUCCESS")
        else:
            self.log_action(username, "LIST_DIR", path, "DENY")

    def delete(self, username, path):
        if path not in self.file_system:
            self.log_action(username, "DELETE", path, "DENY")
            return

        parent = "/".join(path.rstrip("/").split("/")[:-1])
        if username == self.file_system[path]["owner"] or (parent in self.file_system and self.has_permission(username, self.file_system[parent]["permissions"], "W")):
            if path in self.file_system[parent]["contents"]:
                self.file_system[parent]["contents"].remove(path)
            del self.file_system[path]
            self.log_action(username, "DELETE", path, "SUCCESS")
        else:
            self.log_action(username, "DELETE", path, "DENY")

# Example usage
sfs = SecureFileSystem()

# Input processing
u = int(input())
for _ in range(u):
    sfs.add_user(input().strip())

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "CREATE_DIR":
        sfs.create_dir(command[1], command[2], command[3])
    elif command[0] == "CREATE_FILE":
        sfs.create_file(command[1], command[2], command[3])
    elif command[0] == "READ_FILE":
        sfs.read_file(command[1], command[2])
    elif command[0] == "WRITE_FILE":
        sfs.write_file(command[1], command[2])
    elif command[0] == "LIST_DIR":
        sfs.list_dir(command[1], command[2])
    elif command[0] == "DELETE":
        sfs.delete(command[1], command[2])