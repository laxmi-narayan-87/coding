//factorial
int factorial(int n)
{if (n==0)
return 1;
else
return n*factorial(n-1);
}

//fibonacci series
int fibonacci(int n)
{if (n==1)
return 0;
if (n==2)
return 1;
else
return fibonacci(n-1)+fibonacci(n-2);
}

// power or exponential
int power(int a, int b)
{
	if(b==0)
	return 1;
	else 
	return a*power(a,b-1);
	
}

// binary to decimal
int bin_to_dec(int bin)
{
    int dec = 0; 
    int i = 0; 
    while (bin > 0) 
    {
        int rem = bin % 10; 
        bin = bin / 10; 
        dec = dec + rem * pow(2, i);
        i++; 
    }
    return dec;
}

// decimal to binary
int dec_to_bin(int dec)
{
    int bin = 0;
    int i = 1;
    while (dec > 0) 
    {
        int rem = dec % 2; 
        dec = dec / 2; 
        bin = bin + rem * i; 
        i = i * 10; 
    }
    return bin; 
}

// decimal to octal
int dec_to_oct(int dec)
{
    int oct = 0; 
    int i = 1; 
    while (dec > 0) 
    {
        int rem = dec % 8; 
        dec = dec / 8; 
        oct = oct + rem * i; 
        i = i * 10;
    }
    return oct; 
}

// octal to decimal
int oct_to_dec(int oct)
{
    int dec = 0; 
    int i = 0; 
    while (oct > 0) 
    {
        int rem = oct % 10; 
        oct = oct / 10; 
        dec = dec + rem * pow(8, i); 
        i++; 
    }
    return dec; 
}

// gcd or hcf
int gcd(int a,int b)
    {
        if(a%b==0) return b;
        else return gcd(b,a%b);
    }
    
// sum of n natural terms
int sum(int n)
{if (n==0)
return 0;
else
return n+sum(n-1);
}

// reverse of a number
int reverse(int num) {
    int digit = (int) log10(num);
    if (num == 0)
        return 0;
    return ((num%10 * pow(10, digit)) + reverse(num/10));
}

// bubblesort
void bubblesort(int a[], int n)
{if (n==1)
return;
for (j=0;j<n-1;j++)
{if (a[j]>a[j+1])
int b=arr[j+1];   // swap
	arr[j+1]=arr[j];
	arr[j]=b;
}
bubblesort(a,n-1);
}

//insertion sort
void insertionsort(int arr[],int n)
{if (n==1)
return;
insertionsort(arr,n-1);
key=arr[n-1];
for(j=i-1;j>=0&&key<arr[j];j--)
arr[j+1]=arr[j];
arr[j+1]=key;
}
//////////////////// PEAK ELEMENT

int peakElement(int arr[], int n)
{
    int low = 0, high = n - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if ((mid == 0 || arr[mid - 1] <= arr[mid]) &&
            (mid == n - 1 || arr[mid + 1] <= arr[mid]))
            return mid;
        if (mid > 0 && arr[mid - 1] >= arr[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }

}


///////////////////


