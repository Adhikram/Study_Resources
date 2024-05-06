package Questions.String;

public class FindLatestTIme {
    public String findLatestTime(String s) {
        char[] str = s.toCharArray();
        if(str[0] == '?'){
        if(str[1] == '?' || str[1] < '2'){
                str[0] = '1';
        }else{
            str[0] = '0';
        }
        }
        if(str[1] == '?'){
            if (str[0] == '1'){
                str[1] = '1';
            }else{
                str[1] = '9';
            }
        }
        if (str[3] == '?'){
            str[3] = '5';
        }
        if(str[4] == '?'){
            str[4] = '9';
        }
        return new String(str);
    }
    public static void main(String[] args) {
        FindLatestTIme findLatestTIme = new FindLatestTIme();
        String s = "1?:?8";
        System.out.println(findLatestTIme.findLatestTime(s));
    }
}
