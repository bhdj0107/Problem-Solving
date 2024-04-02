import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        System.out.println(getOrder(N, r, c));
    }

    static int getOrder(int N, int r, int c) {
        int box[][] = {{0, 1}, {2, 3}};
        if (N == 1) {
            return box[r][c];
        } else {
            int half = (int)Math.pow(2, N - 1);
            
            int isRowOver = r >= half?1:0;
            int isColOver = c >= half?1:0;

            int ret = (int)Math.pow(half, 2) * box[isRowOver][isColOver];
            ret += getOrder(N - 1, r - isRowOver * half, c - isColOver * half);

            return ret;
        }
    }
}