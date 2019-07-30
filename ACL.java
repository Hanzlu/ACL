//Advanced Computer Language interpreter

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class ACL {
  
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
  
  static int toBin(String dec) {
    int l = dec.length();
    int j = l-1;
    int x = 0;
    int bin = 0;
    while (x < l) {
      bin += Math.pow(2, x) * ((int) dec.charAt(j) - 48);
      x++; j--;
    }
    return bin;
  }
  
  public static void main(String[] args) {
  
    String code = getCode();
    int l = code.length();
    int i = 0; //code reader pointer; 
    
    ArrayList<Byte> memory = new ArrayList<Byte>(); //cell based, binary
    int ptr = -1; //memory pointer
    int cells = 0; //cells in memory
    
    String bOutput = ""; //binary output
    String cOutput = ""; //character output
    char c; //code command
    
    Scanner input = new Scanner(System.in);
    String f = ""; //for functions
    
    //temporary variables
    String t;
    int x;
    
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
              else if (code.charAt(i) == '7' || code.charAt(i) == '8' || (x == 1 && code.charAt(i) == '6')) {
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
            else if (code.charAt(i) == '7' || code.charAt(i) == '8') {
              x--;
            }
          }
          break;
          
        //loop  
        case '8':
          if (memory.get(ptr) == 1) {
            x = 1;
            i--;
            while (x != 0) {
              i--;
              if (code.charAt(i) == '7' || code.charAt(i) == '8') {
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
            cOutput += toBin(bOutput);
          }
          else {
            cOutput += (char) toBin(bOutput);
          }
          bOutput = "";
          break;
          
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
          
        case 'F':
          System.out.println(1111);
          i = l;
      }
     
      i++;
    }  
  input.close();
  }
}
