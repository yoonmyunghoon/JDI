package NHN;

import java.util.Scanner;

public class prob1 {

	private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames,
			int[] numOfMovesPerGame) {
		// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
		int nowIndex = 0;
		char player = 'A';
		char[] seats = new char[numOfAllPlayers - 1];
		int[][] checkBoard = new int[2][numOfAllPlayers];
		checkBoard[0][0] = 1;

		for (int i = 0; i < numOfQuickPlayers; i++) {
			int check = (int) namesOfQuickPlayers[i] - 65;
			checkBoard[1][check] = 1;
		}

		for (int i = 0; i < numOfAllPlayers - 1; i++) {
			seats[i] = (char) (66 + i);
		}

		for (int i = 0; i < numOfGames; i++) {
			int moveCnt = numOfMovesPerGame[i];
			if (nowIndex + moveCnt >= 0) {
				nowIndex = (nowIndex + moveCnt) % (numOfAllPlayers - 1);
			} else {
				nowIndex = (numOfAllPlayers - 1) - (((nowIndex + moveCnt) * (-1)) % (numOfAllPlayers - 1));
			}

			char newPlayer = seats[nowIndex];
			if (checkBoard[1][(int) newPlayer - 65] == 1) {
				checkBoard[0][(int) player - 65] += 1;
			} else {
				checkBoard[0][(int) newPlayer - 65] += 1;
				seats[nowIndex] = player;
				player = newPlayer;
			}

		}

		for (int i = 0; i < numOfAllPlayers - 1; i++) {
			System.out.print(seats[i] + " ");
			System.out.print(checkBoard[0][(int) seats[i] - 65]);
			System.out.println();
		}
		System.out.print(player + " ");
		System.out.print(checkBoard[0][(int) player - 65]);

	}

	private static class InputData {
		int numOfAllPlayers = 6;
		int numOfQuickPlayers = 2;
		char[] namesOfQuickPlayers = { 'B', 'C' };
		int numOfGames = 2;
		int[] numOfMovesPerGame = { 3, -2 };
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = new InputData();

		solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers,
				inputData.numOfGames, inputData.numOfMovesPerGame);
	}

}
