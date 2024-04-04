import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            HashMap<String, HashSet<String>> hm = new HashMap<>();
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String type = st.nextToken();
                if (!hm.containsKey(type)) hm.put(type, new HashSet<String>());
                hm.get(type).add(name);
            }
            int cnt = 1;
            for (String s : hm.keySet()) cnt = cnt * (hm.get(s).size() + 1);
            cnt -= 1;
            System.out.println(cnt);
        }
    }
}