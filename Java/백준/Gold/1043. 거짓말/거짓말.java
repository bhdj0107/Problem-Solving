import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        int O = Integer.parseInt(st.nextToken());
        for (int i = 0; i < O; i++) q.add(Integer.parseInt(st.nextToken()));

        boolean personChked[] = new boolean[N + 1];

        LinkedList<Integer> person2parties[] = new LinkedList[N + 1];
        for (int i = 0; i < N + 1; i++) person2parties[i] = new LinkedList<>();

        LinkedList<Integer> party2person[] = new LinkedList[M];
        for (int i = 0; i < M; i++) party2person[i] = new LinkedList<>();
        boolean isTrueParty[] = new boolean[M];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int P = Integer.parseInt(st.nextToken());
            for (int j = 0; j < P; j++) {
                int thisPerson = Integer.parseInt(st.nextToken());
                person2parties[thisPerson].add(i);
                party2person[i].add(thisPerson);
            }
        }


        while (!q.isEmpty()) {
            // System.out.println("==================");
            // System.out.println(q);
            // System.out.println(Arrays.toString(isTrueParty));
            // System.out.println("---------------");
            int nowPerson = q.remove();
            if (personChked[nowPerson]) continue;
            else {
                personChked[nowPerson] = true;
                LinkedList<Integer> chkParty = person2parties[nowPerson];
                for (int i = 0; i < chkParty.size(); i++) {
                    int thisPartyNum = chkParty.get(i);
                    if (isTrueParty[thisPartyNum]) continue;
                    else {
                        isTrueParty[thisPartyNum] = true;
                        LinkedList<Integer> updatePeople = party2person[thisPartyNum];
                        for (int j = 0; j < updatePeople.size(); j++) q.add(updatePeople.get(j));
                    }
                }
            }
            // System.out.println(q);
            // System.out.println(Arrays.toString(isTrueParty));
            // System.out.println("==================");
        }

        int cnt = 0;
        for (int i = 0; i < M; i++) cnt += isTrueParty[i]?0:1;
        System.out.println(cnt);
    }
}
