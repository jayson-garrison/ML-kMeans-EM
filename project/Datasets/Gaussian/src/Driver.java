import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Vector;



public class Driver {
	static int fileNo=1;
	public static void main(String[] args) {
		// Experiment 1: ===============================================
		// 3 sources
		generateWithParameters(3, 1000, .5, 1, 1, "File"+fileNo+".txt"); 		// 1
		generateWithParameters(3, 1000, 1, 1, 1, "File"+fileNo+".txt");			// 2
		generateWithParameters(3, 1000, 1.5, 1, 1, "File"+fileNo+".txt");		// 3
		generateWithParameters(3, 1000, 2, 1, 1, "File"+fileNo+".txt"); 		// 4
		// 5 sources
		generateWithParameters(5, 1000, .5, 1, 1, "File"+fileNo+".txt"); 		// 5
		generateWithParameters(5, 1000, 1, 1, 1, "File"+fileNo+".txt");			// 6
		generateWithParameters(5, 1000, 1.5, 1, 1, "File"+fileNo+".txt");		// 7
		generateWithParameters(5, 1000, 2, 1, 1, "File"+fileNo+".txt"); 		// 8
		// 10 sources
		generateWithParameters(10, 1000, .5, 1, 1, "File"+fileNo+".txt");		// 9
		generateWithParameters(10, 1000, 1, 1, 1, "File"+fileNo+".txt");		// 10
		generateWithParameters(10, 1000, 1.5, 1, 1, "File"+fileNo+".txt");		// 11
		generateWithParameters(10, 1000, 2, 1, 1, "File"+fileNo+".txt");		// 12

		// Experiment 2: ===============================================
		generateWithParameters(5, 1000, 3, 1, 1, "File"+fileNo+".txt");			// 13
		generateWithParameters(5, 1000, 3, 2, 2, "File"+fileNo+".txt");			// 14
		generateWithParameters(5, 1000, 3, 3, 3, "File"+fileNo+".txt");			// 15

		// Experiment 3: ===============================================
		generateWithParameters(5, 1000, 1.25, 0.75, 2, "File"+fileNo+".txt");	// 16

		// Experiment 4: ===============================================
		generateWithParameters(5, 100, 1.25, .75, .75, "File"+fileNo+".txt");	// 17
		generateWithParameters(5, 1000, 1.25, .75, .75, "File"+fileNo+".txt");	// 18
		generateWithParameters(5, 5000, 1.25, .75, .75, "File"+fileNo+".txt");	// 19
		
		
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
