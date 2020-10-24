package NHN;

import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;

public class example {

	private static int[] dx = { -1, 0, 1, 0 };
	private static int[] dy = { 0, 1, 0, -1 };
	private static int[][] map;
	private static int[][] visited;

	private static class Node {
		int x;
		int y;

		Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	private static void DFS(int x, int y, int count, int size) {
		Queue<Node> queue = new LinkedList<Node>();
		queue.add(new Node(x, y));
		visited[x][y] = count;
		while (!queue.isEmpty()) {
			Node n = queue.poll();
			x = n.x;
			y = n.y;
			for (int i = 0; i < dx.length; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < size && 0 <= ny && ny < size) {
					if (map[nx][ny] == 1 && visited[nx][ny] == 0) {
						visited[nx][ny] = count;
						queue.add(new Node(nx, ny));
					}
				}
			}
		}
	}

	private static void solution(int sizeOfMatrix, int[][] matrix) {
		// TODO: 이곳에 코드를 작성하세요.
		map = matrix;
		visited = new int[sizeOfMatrix][sizeOfMatrix];

		int cnt = 0;

		for (int i = 0; i < sizeOfMatrix; i++) {
			for (int j = 0; j < sizeOfMatrix; j++) {
				if (matrix[i][j] == 1 && visited[i][j] == 0) {
					cnt += 1;
					DFS(i, j, cnt, sizeOfMatrix);
				}
			}
		}

		if (cnt == 0) {
			System.out.println(cnt);
		} else {
			ArrayList<Integer> counts = new ArrayList<Integer>();
			for (int c = 1; c <= cnt; c++) {
				int count = 0;
				for (int i = 0; i < sizeOfMatrix; i++) {
					for (int j = 0; j < sizeOfMatrix; j++) {
						if (visited[i][j] == c) {
							count += 1;
						}
					}
				}
				counts.add(count);
			}
			System.out.println(cnt);
			Collections.sort(counts);
			for (int i = 0; i < cnt; i++) {
				System.out.print(counts.get(i) + " ");
			}
		}

	}

	private static class InputData {
		int sizeOfMatrix;
		int[][] matrix;
	}

	private static InputData processStdin() {
		InputData inputData = new InputData();

		try (Scanner scanner = new Scanner(System.in)) {
			inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

			inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
			for (int i = 0; i < inputData.sizeOfMatrix; i++) {
				String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
				for (int j = 0; j < inputData.sizeOfMatrix; j++) {
					inputData.matrix[i][j] = Integer.parseInt(buf[j]);
				}
			}
		} catch (Exception e) {
			throw e;
		}

		return inputData;
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = processStdin();

		solution(inputData.sizeOfMatrix, inputData.matrix);
	}
}
