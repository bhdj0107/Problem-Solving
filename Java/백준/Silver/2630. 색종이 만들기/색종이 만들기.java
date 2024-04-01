import java.io.*;
import java.util.*;

class OriginalPaper {
    public Boolean cells[][];
    public int size;
    OriginalPaper(int N) {
        cells = new Boolean[N][N];
        size = N;
    }

    void setCell(Boolean value, int x, int y) {
        cells[y][x] = value;
    }

    Boolean getCell(int x, int y) {
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
        int[] count = {0, 0};

        String thisColor = this.checkIsthisPerfect();
        if (thisColor.equals("Not")) {
            SplittedPaper smallPiece;
            int[] splitCnt;
            int delta = size / 2;

            smallPiece = new SplittedPaper(sourcePaper, left, top, right - delta, bottom - delta);
            splitCnt = smallPiece.countPerfectPiece();
            count[0] += splitCnt[0];
            count[1] += splitCnt[1];

            smallPiece = new SplittedPaper(sourcePaper, left + delta, top, right, bottom - delta);
            splitCnt = smallPiece.countPerfectPiece();
            count[0] += splitCnt[0];
            count[1] += splitCnt[1];

            smallPiece = new SplittedPaper(sourcePaper, left, top + delta, right - delta, bottom);
            splitCnt = smallPiece.countPerfectPiece();
            count[0] += splitCnt[0];
            count[1] += splitCnt[1];

            smallPiece = new SplittedPaper(sourcePaper, left + delta, top + delta, right, bottom);
            splitCnt = smallPiece.countPerfectPiece();
            count[0] += splitCnt[0];
            count[1] += splitCnt[1];
            
            return count;
        } else {
            if (thisColor.equals("Blue")) {
                count[0] += 1;
            } else {
                count[1] += 1;
            }
            return count;
        }
    }

    private String checkIsthisPerfect() {
        Boolean firstCell = sourcePaper.getCell(left, top);
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
            return firstCell?"Blue":"White";
        } else {
            return "Not";
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
                OriPaper.setCell(Integer.parseInt(st.nextToken())==1, j, i);
            }
        }
        SplittedPaper sp = new SplittedPaper(OriPaper, 0, 0, N, N);
        int[] ans = sp.countPerfectPiece();
        System.out.println(ans[1]);
        System.out.println(ans[0]);
    }
}