package NHN;

public class prob2 {

	private static void solution(int day, int width, int[][] blocks) {
		// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
		int cnt = 0;
		int[] building = new int[width]; 

		for (int i = 0; i < day; i++) {
			for (int j = 0; j < width; j++) {
				building[j] = building[j] + blocks[i][j];
			}
			for (int j = 1; j < width - 1; j++) {
				int h = building[j];
				int max_l = 0;
				int max_r = 0;
				for (int l = j; l >= 0; l--) {
					if (max_l < building[l]) {
						max_l = building[l];
					}
				}
				for (int r= j; r < width; r++) {
					if (max_r < building[r]) {
						max_r = building[r];
					}
				}
				if (h<max_l && h< max_r) {
					if (max_l < max_r) {
						cnt += (max_l-h);
						building[j] = max_l;
					} else {
						cnt += (max_r-h);
						building[j] = max_r;
					}
				}
			}
		}
		System.out.println(cnt);

	}

	private static class InputData {
		int day = 2;
		int width = 6;
		int[][] blocks = { { 6, 2, 11, 0, 3, 5 }, { 6, 3, 0, 9, 0, 5 } };
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = new InputData();

		solution(inputData.day, inputData.width, inputData.blocks);
	}

}
