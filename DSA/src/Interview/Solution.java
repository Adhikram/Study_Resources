package Interview;

import javax.xml.transform.Result;
import java.util.HashMap;

public class Solution {
    public static HashMap<String, String> createAlphabetMap() {
        HashMap<String, String> map = new HashMap<>();

        for (int i = 1; i <= 26; i++) {
            char letter = (char) ('A' + i - 1); // Convert number to uppercase letter
            map.put(String.valueOf(i), String.valueOf(letter));
        }

        return map;
    }

    public static int decode(String str, HashMap<String, String> store){
        System.out.println("String " + str);
        int result = 0;
        if(store.isEmpty()){
            return 0;
        }
        if(store.containsKey(str)){
            result = 1;
        }
        int n = str.length() ;
        for(int part = 1 ; part < n; part++ ){
            System.out.println("Part " + part);
            System.out.println("left Part " + str.substring(0, part));
            System.out.println("Right Part " + str.substring(part, n));
            int rightPart = decode(str.substring(part, n), store);

            result += rightPart;
        }
        System.out.println("Result " + result);
        return result;
    }

    public static void main(String[] args) {
        //"121" -> "ABA", "AU", "LA" -> 3
        //"1234" -> "ABCD", "LCD", "AWD" -> 3
        //“96” -> “IF” -> 1
        //“90” → 0

        HashMap<String, String> store = createAlphabetMap();
//        store.forEach((k,v)-> System.out.println("Key " + k + " Val " + v));
        System.out.println(decode("121", store));
        System.out.println(decode("1234", store));


    }
}
