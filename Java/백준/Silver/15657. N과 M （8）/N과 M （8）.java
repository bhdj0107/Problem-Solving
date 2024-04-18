import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<Integer> al = new ArrayList<>();
    static int M;
    static int[] outputArray;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        outputArray = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) { al.add(Integer.parseInt(st.nextToken())); }
        Collections.sort(al);
        dfs(0, 0);
        bw.flush();
        bw.close();
    }
    static void dfs(int D, int prevIdx) throws IOException{
        if (D == M) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < M - 1; i++) { sb.append(outputArray[i]); sb.append(" "); }
            sb.append(outputArray[M - 1]);
            sb.append("\n");
            bw.write(sb.toString());
        } else {
            for (int i = prevIdx; i < al.size(); i++) {
                outputArray[D] = al.get(i);
                dfs(D + 1, i);
            }
        }
    }
}