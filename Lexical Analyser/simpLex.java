import java.util.*;
import java.io.*;
import java.lang.*;


public class simpLex{
	
	public static void main(String[] args){
		try{
			File file = new File(args[0]);
			FileInputStream fis = new FileInputStream(file);
			lex lexeme = new lex();
			while (fis.available() > 0){
				lexeme.check(fis);
			}
		}
		catch(Exception e){
			System.out.println("File Not Found");
		}
	}

}
