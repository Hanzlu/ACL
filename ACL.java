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
    
    String output = "";
    char c; //code command
    
    Scanner input = new Scanner(System.in);
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
          output += memory.get(ptr);
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
              else if (code.charAt(i) == '7' || code.charAt(i) == 'E' || (x == 1 && code.charAt(i) == '6')) {
                x--;
              }
            }
          }
          break;
        case '6':
          x = 1;
          while (x != 0) {
            i++;
            if (code.charAt(i) == '5') {
              x++;
            }
            else if (code.charAt(i) == '7' || code.charAt(i) == 'E') {
              x--;
            }
          }
          break;
          
        case '8':
          memory.set(ptr,(byte) 0);
          break;
        
        case '9':
          memory.set(ptr,(byte) Math.round(Math.random()));
          break;
          
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
          System.out.println(output);
          output = "";
          break;
       
        //integer and character output
        case 'C':
          if (memory.get(ptr) == 1) {
            System.out.println(toBin(output));
          }
          else {
            System.out.println((char) toBin(output));
          }
          output = "";
          break;
          
        //comment  
        case 'D':
          i++;
          while (code.charAt(i) != 'D') {
            i++;
          }
          break;
          
        //loop  
        case 'E':
          if (memory.get(ptr) == 1) {
            x = 1;
            i--;
            while (x != 0) {
              i--;
              if (code.charAt(i) == '7' || code.charAt(i) == 'E') {
                x++;
              }
              else if (code.charAt(i) == '5') {
                x--;
              }
            }
          }
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