import java.util.*;
import java.io.*;
import java.lang.*;

public class Comm{

	public static String wordco = "";

	public static String checkco(FileInputStream fis) throws IOException {
		wordco = "";
		while (!(lex.ch == '\n')){
			lex.ch = (char)fis.read();
			wordco = wordco + lex.ch;
		}
		return wordco;
	}

}
