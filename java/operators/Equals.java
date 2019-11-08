class Equals { 
  public void equals(int[] toSum, int num) {
    if (toSum[0] + toSum[1] == num) {
      System.out.println("Equal");
    } else {
      System.out.println("Not Equal");
    }
  }
  public static void main(String args[]) { 
    int[] toSum = {2, 7};
    int num = 9;
    Equals eql = new Equals();
    eql.equals(toSum, num);
  } 
}; 
