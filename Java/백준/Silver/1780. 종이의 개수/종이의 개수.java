import java.io.*;
import java.util.*;

class OriginalPaper {
    public int cells[][];
    public int size;
    OriginalPaper(int N) {
        cells = new int[N][N];
        size = N;
    }

    void setCell(int value, int x, int y) {
        cells[y][x] = value;
    }

    int getCell(int x, int y) {
        return cells[y][x];
    }
}

class SplittedPaper {
    public OriginalPaper sourcePaper;
    public int left;
    public int top;
    public int right;
    public int bottom;
    public int size;
    SplittedPaper(OriginalPaper source, int left, int top, int right, int bottom) {
        sourcePaper = source;
        this.left = left;
        this.top = top;
        this.right = right;
        this.bottom = bottom;

        size = right - left;
    }

    public int[] countPerfectPiece() {
        // B, W
        int[] count = {0, 0, 0};

        int thisColor = this.checkIsthisPerfect();
        if (thisColor == -2) {
            SplittedPaper smallPiece;
            int[] splitCnt;
            int delta = size / 3;

            for (int i = 0; i < 9; i++) {
                int newLeft = left + delta * (i % 3);
                int newTop = top + delta * (i / 3);
                smallPiece = new SplittedPaper(sourcePaper, newLeft, newTop, newLeft + delta, newTop + delta);
                splitCnt = smallPiece.countPerfectPiece();
                count[0] += splitCnt[0];
                count[1] += splitCnt[1];
                count[2] += splitCnt[2];
            }

            return count;
        } else {
            thisColor += 1;
            count[thisColor] += 1;
            return count;
        }
    }

    private int checkIsthisPerfect() {
        int firstCell = sourcePaper.getCell(left, top);
        Boolean isPerfect = true;
        for (int i = top; i < bottom; i++) {
            for (int j = left; j < right; j++) {
                if (sourcePaper.getCell(j, i) != firstCell) {
                    isPerfect = false;
                    break;
                }
            }
            if (!isPerfect) break;
        }
        if (isPerfect) {
            return firstCell;
        } else {
            return -2;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        int N = Integer.parseInt(br.readLine());
        OriginalPaper OriPaper = new OriginalPaper(N);
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                OriPaper.setCell(Integer.parseInt(st.nextToken()), j, i);
            }
        }
        SplittedPaper sp = new SplittedPaper(OriPaper, 0, 0, N, N);
        int[] ans = sp.countPerfectPiece();
        for (int i = 0; i < 3; i++)
        System.out.println(ans[i]);
    }
}