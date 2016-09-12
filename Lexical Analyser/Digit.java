import java.util.*;
import java.io.*;
import java.lang.*;

public class Digit{
	public static String wordd = "";
	public static int z = 0;


	public static String checkd(FileInputStream fis) throws IOException {
		wordd = "";
		z=0;
		while (Character.isDigit(lex.ch) || lex.ch == '.' || Character.isLetter(lex.ch)){
			if (Character.isDigit(lex.ch)){
				wordd = wordd + lex.ch;
				lex.ch = (char)fis.read();
			} else if(lex.ch == '.') {
				z += 1;
				wordd = wordd + lex.ch;
				lex.ch = (char)fis.read();
				if (!(Character.isDigit(lex.ch))){
					return "-100asd#12-+qw2s5d412@@#$";
				}
			} else{
				z = 10000;
				wordd = wordd + lex.ch;
				lex.ch = (char)fis.read();
			}
		}
		if (z == 1 || z == 0){
			return wordd;
		} else if (z<10000){
			return "-1hypvar!@4";
		} else{
			return "-10ypvar!68&&*^";
		}
	}
	
}
