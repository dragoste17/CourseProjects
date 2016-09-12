import java.util.*;
import java.io.*;
import java.lang.*;

public class lex{
	public static String word = "";
	public static char ch = ' ';
	
	public static void check(FileInputStream fis) throws IOException {
		word = "";
		getNonSpace(fis);
		if (Character.isLetter(ch)){
			Letter objl = new Letter();
			word = objl.checkl(fis);
			if (objl.a == 1){
				System.out.printf("KEY \t \t %s \n",word);
			} else if (objl.a == 0) {
				System.out.printf("IDENT \t \t %s \n",word);
			} else {
				System.out.printf("Unexpected symbol %s in the identifier name: %s\n",word,Letter.wordl);
				ch = (char)fis.read();
			}
		} else if (Character.isDigit(ch)){
			Digit objd = new Digit();
			word = objd.checkd(fis);
			if (word == "-1hypvar!@4"){
				System.out.printf("Unexpected period sign(s) '.' in %s\n", Digit.wordd);
			} else if (word == "-10ypvar!68&&*^"){
				System.out.printf("Unexpected letter(s) in the numeical value, %s\n",Digit.wordd);
			} else if (word == "-100asd#12-+qw2s5d412@@#$"){
				System.out.printf("Unexpected decimal mark in %s\n",Digit.wordd);
			} else {
				System.out.printf("DIGIT \t \t %s \n",word);
			}
		} else if (ch=='\"'){
			Stringie objs = new Stringie();
			word = objs.checks(fis);
			if (word == "-+infhyp*/"){
				System.out.println("String ending by double quotes (\") is missing");
			}else{
				System.out.printf("STRING \t \t %s \n",word);
			}
		} else if (ch=='/'){
			ch = (char)fis.read();
			if (ch=='*'){
				Comment objc = new Comment();
				word = objc.checkc(fis);
				if (word == "-1"){
					System.out.println("Expected '*/' at the end of the comment");
				} else {
					System.out.printf("COMMENT \t%s \n",word);
				}
			} else if (ch=='/'){
				Comm objco = new Comm();
				word = objco.checkco(fis);
				System.out.printf("COMMENT \t %s \n",word);
			} else {
				System.out.println("DIV_OP \t \t /");
			}
		} else {
			Unknown obju = new Unknown();
			obju.checku(fis);
		}
	}

	public static void getNonSpace(FileInputStream fis) throws IOException{
		while (Character.isWhitespace(ch)){
			ch = (char)fis.read();
		}
	}

}
