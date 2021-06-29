class Solution {
    public long solution(int a, int b) {
      long answer = 0;
      if(a <= b)   {
          for(int i=a; i<=b; i++)   {
              answer += i;
          }
      }
      else  {
          for(int i=a; i>=b; i--)    {
              answer += i;
          }
      }
      return answer;
    }
}

// 배울만한 다른 해결방법
class Solution {
  public long solution(int a, int b) {
      long answer = 0;
      for (int i = ((a < b) ? a : b); i <= ((a < b) ? b : a); i++) 
          answer += i;

      return answer;
  }
}