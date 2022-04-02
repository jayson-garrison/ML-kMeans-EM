import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Vector;



public class Driver {
	static int fileNo=1;
	public static void main(String[] args) {
		// Experiment 1
		generateWithParameters(3, 1000, 0.5,1,1, "File"+fileNo+".txt");
		generateWithParameters(3, 1000, 1,1,1, "File"+fileNo+".txt");
		generateWithParameters(3, 1000, 1.5,1,1, "File"+fileNo+".txt");
		generateWithParameters(5, 1000, 0.5,1,1, "File"+fileNo+".txt");
		generateWithParameters(5, 1000, 1,1,1, "File"+fileNo+".txt");
		generateWithParameters(5, 1000, 1.5,1,1, "File"+fileNo+".txt");
		generateWithParameters(7, 1000, 0.5,1,1, "File"+fileNo+".txt");
		generateWithParameters(7, 1000, 1,1,1, "File"+fileNo+".txt");
		generateWithParameters(7, 1000, 1.5,1,1, "File"+fileNo+".txt");
		// Experiment 2
		generateWithParameters(3, 1000, 1.25,2,2, "File"+fileNo+".txt");
		generateWithParameters(3, 1000, 1.25,5,5, "File"+fileNo+".txt");
		generateWithParameters(3, 1000, 1.25,10,10, "File"+fileNo+".txt");
		// Experiment 3
		generateWithParameters(3, 1000, 1.25,0.75,2, "File"+fileNo+".txt");
		// Experiment 4
		generateWithParameters(3, 100, 1,1,1, "File"+fileNo+".txt");
		generateWithParameters(3, 1000, 1,1,1, "File"+fileNo+".txt");
		generateWithParameters(3, 10000, 1,1,1, "File"+fileNo+".txt");
		
		
	} 

	public static void generateWithParameters(int noOfGenerators,int noOfPoints,double delta,double minStDev,double maxStDev,String fileName)
	{
		fileNo++;
		Vector<GaussianRandomGenerator> generators = new Vector<GaussianRandomGenerator>();
		String s ="";
		Random rand = new Random();// You can seed this Object to allow the generators to be picked in the same order at each run.
		for(int i=0;i<noOfGenerators;i++)
		{
			GaussianRandomGenerator g= new GaussianRandomGenerator(1+(i*delta), minStDev+(rand.nextDouble()*(maxStDev-minStDev)));
			generators.add(g);
			s+=g+"\n";
		}


		for(int i=0;i<noOfPoints;i++)
		{
			int chosenGenerator=rand.nextInt(generators.size());
			GaussianRandomGenerator g = generators.get(chosenGenerator);
			s+= g.mean+"\t"+g.nextDouble()+"\n";
		}
		System.out.println(s);
		write(fileName, s);

	}

	public static void write(String fileName,String s)
	{
		try
		{ 
			System.out.println(fileName);
			File file = new File(fileName);

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(s);
			bw.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
