package Questions.String;

import java.util.HashMap;

public class NumberOfSpecialChar {
    public int numberOfSpecialChars(String word) {
        int dist = 'A' - 'a';
        int result = 0;
        HashMap<Integer, Boolean> hash = new HashMap<>();

        for (char ch : word.toCharArray()) {
            hash.put(ch - 'a', true);
            hash.forEach((k, v) -> System.out.println(k + " " + v));
        }

        for (int i = 0; i < 26; i++) {
            if (hash.containsKey(i) && hash.containsKey(i + dist)) {
                result++;
            }
        }

        return result;
    }
    public int numberOfSpecialChars2(String word) {
        int dist = 'a' - 'A';
        int result = 0;
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0 ; i < word.length(); i ++) {
            char ch = word.charAt(i);
            // System.out.println("Char:- " + ch);
            if(hash.containsKey(ch - 'A') && ch >= 'A' && ch <= 'Z' ){
                continue;
            }
            hash.put(ch - 'A', i);
            // hash.forEach((k, v) -> System.out.println(k + " " + v));
            // System.out.println("-----------------------------");
        }

        for (int i = 0; i < 26; i++) {
            if (hash.containsKey(i) && hash.containsKey(i + dist) && hash.get(i) > hash.get(i + dist)) {
                result++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        NumberOfSpecialChar numberOfSpecialChar = new NumberOfSpecialChar();
        String word = "abAc";
        System.out.println(numberOfSpecialChar.numberOfSpecialChars(word));
        System.out.println(numberOfSpecialChar.numberOfSpecialChars2(word));
    }

}
