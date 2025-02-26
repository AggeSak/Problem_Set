class Solution {
    public int romanToInt(String s) {
      int d = s.length();
      int[] a = new int[d] ;
      int k=0;
      for (int i=0; i<d; i++){

           char c = s.charAt(i);

           if (c=='I') {a[i]=1;}
           else if (c=='V') {a[i]=5;}
           else if (c=='X') {a[i]=10;}
           else if (c=='L') {a[i]=50;}
           else if (c=='C') {a[i]=100;}
           else if (c=='D') {a[i]=500;}
           else if (c=='M') {a[i]=1000;}
           else {System.out.println("False Input");}

      } 

      for(int i=0; i<d; i++){
           if (i<d-1 && a[i]<a[i+1] ) k=k-a[i];
           else k=k+a[i];

      }
    return k;
    }
    
}