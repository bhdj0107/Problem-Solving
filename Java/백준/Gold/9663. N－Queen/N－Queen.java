import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int cnt = 0;
    static int N;       
    static int[] dx = {1, 1, 1, 0, 0, -1, -1, -1};
    static int[] dy = {1, 0, -1, 1, -1, 1, 0, -1};
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        char map[][] = new char[N][N];
        nQueen(map, 0);
        System.out.println(cnt);
    }

    static void nQueen(char[][] map, int D) {
        if (D == N) { cnt++; return; }
        else {
            for (int i = 0; i < N; i++) {
                if (map[D][i] > 0) continue;
                else {
                    addQueen(map, D, i);
                    nQueen(map, D + 1);
                    delQueen(map, D, i);
                }
            }
        }
    }

    static void addQueen(char[][] map, int row, int col) {
        if (map[row][col] > 0) return;
        else {
            map[row][col] += 1;
            for (int i = 1; i < N; i++) {
                for (int j = 0; j < 8; j++) {
                    int nCol = col + dx[j] * i;
                    int nRow = row + dy[j] * i;
                    if (nCol < 0 || nCol >= N || nRow < 0 || nRow >= N) continue;
                    map[nRow][nCol] += 1;
                }
            }
        }
    }

    static void delQueen(char[][] map, int row, int col) {
        map[row][col] -= 1;
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < 8; j++) {
                int nCol = col + dx[j] * i;
                int nRow = row + dy[j] * i;
                if (nCol < 0 || nCol >= N || nRow < 0 || nRow >= N) continue;
                map[nRow][nCol] -= 1;
            }
        }
    }

}