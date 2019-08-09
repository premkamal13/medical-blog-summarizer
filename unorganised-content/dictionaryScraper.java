import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.regex.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Dic 
{
 	public static void main(String[] args) throws IOException 
	{ 
    String inputLine,s="";
    int a[]={19,9,21,10,10,9,8,10,9,1,2,10,15,8,6,23,1,9,21,12,4,7,2,1,1,1};
		Pattern patt = Pattern.compile("(<td><li><a href=.*[0-9]\">)(.*)(</a></li></td>)");
			
		File file = new File("C:\\lab\\fms\\Dictionary.txt");
		FileWriter fw = new FileWriter(file.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);
			
		for(int i=97;i<=122;i++)
		{
			String p="http://www.medilexicon.com/medicaldictionary.php?l=";
			char q=(char)i;
			String h= p+q;
			URL x = new URL(h);
			BufferedReader in = new BufferedReader(new InputStreamReader(x.openStream()));
      while ((inputLine = in.readLine()) != null)
      { 
			  Matcher m = patt.matcher(inputLine);
        while (m.find())
        {
		 			bw.write(m.group(2)+"\n");
      	}
			}
			in.close();
			if(a[i-97]>1)
			{
				for(int j=2;j<=a[i-97];j++)
			  {
			   	p="http://www.medilexicon.com/medicaldictionary.php?l=";
					q=(char)i;
					h= p+q+"&s=&p="+Integer.toString(j);
			 		URL x2 = new URL(h);
			  	BufferedReader in2 = new BufferedReader(new InputStreamReader(x2.openStream()));
          while ((inputLine = in2.readLine()) != null)
          { 
			   		Matcher m2 = patt.matcher(inputLine);
         		while (m2.find())
         		{
		 					bw.write(m2.group(2)+"\n");
            }
				  }		  
			  }
			  in.close();
		  } 
		}
		bw.close();        
	}
}