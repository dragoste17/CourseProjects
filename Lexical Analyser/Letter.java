import java.util.*;
import java.io.*;
import java.lang.*;

public class Letter{
	public static String wordl = "";
	public static int a=-1;
	
	public static String checkl(FileInputStream fis) throws IOException {
		wordl = "";
		while (Character.isLetter(lex.ch) || Character.isDigit(lex.ch) || lex.ch == '_'){
			wordl = wordl + lex.ch;
			lex.ch = (char)fis.read();
		}
		if (Character.isWhitespace(lex.ch) || lex.ch == '/' || lex.ch=='+' || lex.ch=='-' || lex.ch=='*' || lex.ch=='%' || lex.ch=='=' || lex.ch=='}' || lex.ch=='!' || lex.ch=='<' || lex.ch=='>' || lex.ch==')' || lex.ch=='(' || lex.ch=='{' || lex.ch==',' || lex.ch==';' || lex.ch==':' || lex.ch=='.' || lex.ch=='?'){
			a = lookup(wordl.toLowerCase());
			return wordl;
		} else {
			a=-1;
			String s = Character.toString(lex.ch);
			wordl += s;
			return s;
		}
	}
	
	public static int lookup(String wordl){
		if (wordl.equals("and") || wordl.equals("if") || wordl.equals("bool") || wordl.equals("const") || wordl.equals("do") || wordl.equals("else") || wordl.equals("false") || wordl.equals("int") || wordl.equals("main") || wordl.equals("not") || wordl.equals("or") || wordl.equals("real") || wordl.equals("return") || wordl.equals("string") || wordl.equals("then") || wordl.equals("true") || wordl.equals("var") || wordl.equals("void") || wordl.equals("while")){
			return 1;
		} else {
			return 0;
		}
	}

}
