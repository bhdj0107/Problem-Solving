import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String S = br.readLine();
        String bomb = br.readLine();
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < S.length(); i++) {
            sb.append(S.charAt(i));
            int sbLen = sb.length();
            if (sbLen < bomb.length()) continue;
            if (bomb.equals(sb.substring(sbLen - bomb.length(), sbLen))) {
                sb.delete(sbLen - bomb.length(), sbLen);
            }
        }
        String ans = sb.toString();
        if (ans.equals("")) System.out.println("FRULA");
        else System.out.println(ans);
    }
}