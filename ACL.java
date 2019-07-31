//Advanced Computer Language interpreter

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class ACL {
  
  //reads source file and returns the code
  static String getCode() {
    try {
      Scanner getName = new Scanner(System.in);
      System.out.println("File to interpret?");
      String fileName = getName.nextLine();
      getName.close();
    
      File file = new File(fileName);
      Scanner fRead = new Scanner(file);
      String code = fRead.nextLine();
      fRead.close();
    
      return code;
    } catch (FileNotFoundException e) {
      System.out.println("FILE FAIL");
      return "F";
    }
  }
 
  //binary to decimal
  static int toDec(String bin) {
    int l = bin.length();
    int j = l-1;
    int x = 0;
    int dec = 0;
    while (x < l) {
      dec += Math.pow(2, x) * ((int) bin.charAt(j) - 48);
      x++; j--;
    }
    return dec;
  }
  
  //--------------------------------------------------------------
  
  public static void main(String[] args) {
  
    //declares necessary variables etc.
    
    String code = getCode();
    int l = code.length();
    int i = 0; //code reader pointer; 
    
    ArrayList<Byte> memory = new ArrayList<Byte>(); //cell based, binary
    memory.add((byte) 0); //make the memory have one cell at start
    int ptr = 0; //memory pointer
    int cells = 1; //cells in memory
    
    String bOutput = ""; //binary output
    String cOutput = ""; //character output
    char c; //code command
    
    Scanner input = new Scanner(System.in);
    String f = ""; //for functions
    
    //temporary variables
    String t;
    int x;
    
    //------------------------------------------------------------------------
    
    //inserts function code when function call
    //pre-execution
    while (i < l) {
      c = code.charAt(i);
      switch (c) {
        //declare function  
        case 'D':
          i++;
          f = "";
          while (code.charAt(i) != 'D') {
            f += code.charAt(i);
            i++;
          }
          break;
        //enter function into code 
        case 'E':
          t = "";
          for (x = 0; x < i+1; x++) {
            t += code.charAt(x);
          }
          t += f;
          for (x = i+1; x < l; x++) {
            t += code.charAt(x);
          }
          code = t;
          l = code.length();
          break;
      }
      i++;
    }
    i = 0;
    
    //--------------------------------------------------------------
    
    //reads and executes the code
    while (i < l) {
      c = code.charAt(i);

      switch (c) {
        
        //pointer movement
        case '0':
          ptr = 0;
          break;
        case '1':
          ptr++;
          if (ptr == cells) {
            memory.add((byte) 0);
            cells++;
          }
          break;
        case '2':
          ptr--;
          if (ptr < 0) {
            ptr = cells - 1;
          } 
          break;
        
        //bit flip
        case '3':
          if (memory.get(ptr) == 1) {
            memory.set(ptr,(byte) 0);
          }
          else {
            memory.set(ptr,(byte) 1);
          }
          break;

        case '4':
          bOutput += memory.get(ptr);
          break;
          
        //if-else-endif  
        case '5':
          if (memory.get(ptr) == 0) {
            x = 1;
            while (x != 0) {
              i++;
              if (code.charAt(i) == '5') {
                x++;
              }
              else if (code.charAt(i) == '7' || (x == 1 && code.charAt(i) == '6')) {
                x--;
              }
            }
          }
          break;
        //else
        case '6':
          x = 1;
          while (x != 0) {
            i++;
            if (code.charAt(i) == '5') {
              x++;
            }
            else if (code.charAt(i) == '7') {
              x--;
            }
          }
          break;
          
        case '7':
          //endif command, does nothing on its own
          break;
          
        //loop  
        case '8':
          if (memory.get(ptr) == 1) {
            x = 1;
            i--;
            while (x != 0) {
              i--;
              if (code.charAt(i) == '7') {
                x++;
              }
              else if (code.charAt(i) == '5') {
                x--;
              }
            }
          }
          break;
        
        case '9':
          memory.set(ptr, (byte) Math.round(Math.random()));

        //input
        case 'A':
          x = Integer.parseInt(input.nextLine());
          if (x != 0 && x != 1) {
            System.out.println(1111);
            i = l;
          }
          else {
            memory.set(ptr,(byte) x);
            break;
          }
        
        //binary output
        case 'B':
          System.out.println(bOutput);
          bOutput = "";
          break;
       
        //integer and character output
        case 'C':
          if (bOutput.equals("")) {
            System.out.println(cOutput);
            cOutput = "";
          }
          else if (memory.get(ptr) == 1) {
            cOutput += toDec(bOutput);
          }
          else {
            cOutput += (char) toDec(bOutput);
          }
          bOutput = "";
          break;
          
        case 'D':
          break;
        case 'E':
          //D and E are handled pre-execution
          break;
          
        case 'F':
          System.out.println(1111);
          i = l;
      }
     
      i++;
    }  
  input.close();
  }
}
