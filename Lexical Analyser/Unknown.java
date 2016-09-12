import java.util.*;
import java.io.*;
import java.lang.*;

public class Unknown{

	public static String wordu = "";
	public static int spcl_counter = 1;

	public static void checku(FileInputStream fis) throws IOException {
		wordu = "";
		spcl_counter = 1;
		switch (lex.ch){
			case '+':
				lex.ch = (char)fis.read();
				System.out.println("ADD_OP \t \t +");
				break;
			case '-':
				lex.ch = (char)fis.read();
				System.out.println("SUB_OP \t \t -");
				break;
			case '*':
				lex.ch = (char)fis.read();
				System.out.println("MUL_OP \t \t *");
				break;
			case '/':
				lex.ch = (char)fis.read();
				System.out.println("DIV_OP \t \t /");
				break;
			case '%':
				lex.ch = (char)fis.read();
				System.out.println("MOD_OP \t \t %");
				break;
			case '=':
				lex.ch = (char)fis.read();
				System.out.println("ASSIGN_OP \t =");
				break;
			case '!':
				lex.ch = (char)fis.read();
				if (lex.ch == '='){
					System.out.println("NOTEQ_OP \t \t !=");
					lex.ch = (char)fis.read();
					break;
				} else {
					System.out.println("NOT \t \t !");
				}
				break;
			case '<':
				lex.ch = (char)fis.read();
				if (lex.ch == '='){
					System.out.println("LESSEQ_OP \t \t <=");
					lex.ch = (char)fis.read();
					break;
				} else {
					System.out.println("LESS_OP \t \t <");
				}
				break;
			case '>':
				lex.ch = (char)fis.read();
				if (lex.ch == '='){
					System.out.println("GREATEQ_OP \t \t >=");
					lex.ch = (char)fis.read();
					break;
				} else {
					System.out.println("GREAT_OP \t \t >");
				}
				break;
			case '(':
				lex.ch = (char)fis.read();
				System.out.println("LEFT_PAREN \t (");
				break;
			case ')':
				lex.ch = (char)fis.read();
				System.out.println("RIGHT_PAREN \t )");
				break;
			case ',':
				lex.ch = (char)fis.read();
				System.out.println("COMMA \t \t ,");
				break;
			case ';':
				lex.ch = (char)fis.read();
				System.out.println("SEMICOLON \t ;");
				break;
			case ':':
				lex.ch = (char)fis.read();
				if (lex.ch == '='){
					System.out.println("COLEQ \t \t :=");
					lex.ch = (char)fis.read();
					break;
				} else {
					System.out.println("COLON \t \t :");
				}
				break;
			case '.':
				lex.ch = (char)fis.read();
				wordu += ".";
				while (Character.isDigit(lex.ch)){
					wordu += lex.ch;
					lex.ch = (char)fis.read();
					spcl_counter = 100;
				}
				if (spcl_counter == 100){
					System.out.printf("Invalid number found %s\n",wordu);
				} else{
					System.out.println("PERIOD \t \t .");
				}
				break;
			case '?':
				lex.ch = (char)fis.read();
				System.out.println("QUES \t \t ?");
				break;
			case '{':
				lex.ch = (char)fis.read();
				System.out.println("LEFT_BRACE \t {");
				break;
			case '}':
				lex.ch = (char)fis.read();
				System.out.println("RIGHT_BRACE \t }");
				break;
			default:
				System.out.printf("Unidentified Symbol %s in the code\n",lex.ch);
				lex.ch = (char)fis.read();
		}
	}

}
