import java.util.*;
import java.io.*;
import java.lang.*;

public class Stringie{
	
	public static String words = "";

	public static String checks(FileInputStream fis) throws IOException {
		words = "";
		lex.ch = (char)fis.read();
		while (fis.available() > 0){
			while (!(lex.ch == '\\') && !(lex.ch == '\"') && fis.available() > 0){
				words = words + lex.ch;
				lex.ch = (char)fis.read();
			}
			if (lex.ch == '\\'){
				lex.ch = (char)fis.read();
				if (lex.ch == '\"'){
					words = words + '\"';
					lex.ch = (char)fis.read();
					continue;
				} else if (lex.ch == '\\'){
					words = words + '\\';
					lex.ch = (char)fis.read();
					continue;
				} else if (lex.ch == 'n'){
					words = words + "\n" + "\t" + "\t";
					lex.ch = (char)fis.read();
					continue;
				} else {
					continue;
				}
			} else{
				break;
			}
		}
		if (fis.available() > 0){
			lex.ch = (char)fis.read();
			return words;
		} else {
			return "-+infhyp*/";
		}
	}

}
