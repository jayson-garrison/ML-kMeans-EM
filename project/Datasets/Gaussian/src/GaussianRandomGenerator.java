

import java.util.Random;

public class GaussianRandomGenerator {
	public double mean;
	public double stDev;
	Random rand;
	public double seed;
	public GaussianRandomGenerator(double mean,double stDev,int seed) 
	{
		this.seed = seed;
		rand = new Random(seed);
		this.mean = mean;
		this.stDev=stDev;
	}
	public GaussianRandomGenerator(double mean,double stDev) 
	{
		rand = new Random();
		this.mean = mean;
		this.stDev=stDev;
	}
	
	public double nextDouble()
	{
		return mean + rand.nextGaussian()*stDev;
	}
	
	@Override
	public String toString() {
		return "Gaussian Generator("+mean+"): mean="+mean+",stDev="+stDev;
	}

}
