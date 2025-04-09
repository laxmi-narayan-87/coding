#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp_read, *fp_write;
    char line[1024];
    char *token;
    const char *delimiter = "+";

    // Open the text file for reading
    fp_read = fopen("contact.txt", "r");
    if (fp_read == NULL) {
        perror("Error opening file");
        return -1;
    }

    // Open the CSV file for writing
    fp_write = fopen("contacts.csv", "w");
    if (fp_write == NULL) {
        perror("Error opening file");
        fclose(fp_read);
        return -1;
    }

    // Write the header row in the CSV file
    fprintf(fp_write, "Contact1,Contact2,Contact3\n");

    // Read each line from the text file
    while (fgets(line, sizeof(line), fp_read)) {
        // Get the contact numbers and write them to the CSV file
        token = strtok(line, delimiter);
        while (token != NULL) {
            fprintf(fp_write, "%s,", token);
            token = strtok(NULL, delimiter);
        }
        fprintf(fp_write, "\n"); // End the row
    }

    // Close the files
    fclose(fp_read);
    fclose(fp_write);

    printf("Contact details have been written to contacts.csv\n");

    return 0;
}

