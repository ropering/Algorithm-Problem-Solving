package p_04_30;
/*
 * 내용: 별 그리기(5개)
 * 사용 기술
 * - 2중 for문
 * 결과
 *  *****
	****
	***
	**
	*
 */

public class MakeStar {
	public static void main(String[] args) {
		for (int i=0; i<=4; i++) {
			
			for (int j=5; j-i > 0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
