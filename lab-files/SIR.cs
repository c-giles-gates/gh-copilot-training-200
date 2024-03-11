public class SIRModel
{
    public double TotalPopulation { get; set; }
    public double InitialInfected { get; set; }
    public double InitialRecovered { get; set; }
    public double Beta { get; set; }
    public double Gamma { get; set; }

    public SIRModel(double totalPopulation, double initialInfected, double initialRecovered, double beta, double gamma)
    {
        TotalPopulation = totalPopulation;
        InitialInfected = initialInfected;
        InitialRecovered = initialRecovered;
        Beta = beta;
        Gamma = gamma;
    }

    // Add methods to calculate the SIR model here
    
}