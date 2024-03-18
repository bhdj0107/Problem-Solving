import java.io.*;
import java.lang.Math;
import java.util.*;

class Solution {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    Boolean[] picked;
    int pickCnt = 0;
    int L, C;
    ArrayList<String> inps = new ArrayList<>();

    public void solution() 
    throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) inps.add(st.nextToken());
        Collections.sort(inps);
        picked = new Boolean[C];
        Arrays.fill(picked, false);
        dfs(0);
        bw.flush();
        bw.close();
    }

    void dfs(int D) throws IOException{
        if (D == C) {
            if (pickCnt == L) {
                printPickedIfIsCorrect();
            }
        }
        else {
            if (pickCnt == L) {
                printPickedIfIsCorrect();
            } else {
                picked[D] = true;
                pickCnt += 1;

                dfs(D + 1);

                picked[D] = false;
                pickCnt -= 1;

                dfs(D + 1);
            }
        }
    }

    void printPickedIfIsCorrect() throws IOException {
        StringBuilder sb = new StringBuilder();
        int vowel = 0;
        int consonant = 0;
        for (int i = 0; i < C; i++) {
            String character = inps.get(i);
            if (picked[i]) {
                Boolean isConsonant = false;
                isConsonant = (isConsonant || character.equals("a"));
                isConsonant = (isConsonant || character.equals("e"));
                isConsonant = (isConsonant || character.equals("i"));
                isConsonant = (isConsonant || character.equals("o"));
                isConsonant = (isConsonant || character.equals("u"));
                sb.append(inps.get(i));
                consonant += isConsonant?1:0;
                vowel += isConsonant?0:1;
            }
        }
        if (consonant >= 1 && vowel >= 2) {
            bw.write(sb.toString());
            bw.write("\n");
        }
    }
}

public class Main {
    public static void main(String[] argv) throws IOException {
        Solution sol = new Solution();
        sol.solution();
    }
}