import java.io.*;
import java.util.*;

class Solution {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public void solution() throws IOException{
        int N = Integer.parseInt(br.readLine());
        boolean inps[] = new boolean[2000001];
        for (int i = 0; i < N; i++) inps[Integer.parseInt(br.readLine())+1000000] = true;
        for (int i = 0; i < 2000001; i++) {
            if (inps[i]) bw.write(i - 1000000 + "\n");
        }
        bw.flush();
        bw.close();
    }
}

public class Main {
    public static void main(String argv[]) throws IOException{
        Solution sol = new Solution();
        sol.solution();
    }
}