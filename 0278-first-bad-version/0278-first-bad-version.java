
public class Solution extends VersionControl {
   public int firstBadVersion(int n) {
    return helper(1, n);
}
 
public int helper(int i, int j){
    int m = i + (j-i)/2;
 
    if(i>=j)
        return i;
 
    if(isBadVersion(m)){
        return helper(i, m);
    }else{
        return helper(m+1, j);
    }
}

}