package Questions.Graph;


import java.util.HashMap;
import java.util.Map;

public class CurrencyExchange {

    private Map<String, String> parent;
    private Map<String, Double> exchangeRate;

    public CurrencyExchange() {
        parent = new HashMap<>();
        exchangeRate = new HashMap<>();
    }

    // Add a new currency with its parent and exchange rate
    public void addCurrency(String currency, String parentCurrency, double rate) {
        parent.put(currency, parentCurrency);
        exchangeRate.put(currency, rate);
        exchangeRate.put(parentCurrency, 1.0);
    }

    // Find the ultimate parent of a currency and update its exchange rate along the
    // path
    private String findUltimateParent(String currency) {
        if (!parent.containsKey(currency)) {
            return currency;
        }
        String ultimateParent = findUltimateParent(parent.get(currency));
        exchangeRate.put(currency, exchangeRate.get(currency) * exchangeRate.get(parent.get(currency)));
        parent.put(currency, ultimateParent);
        return ultimateParent;
    }

    // Calculate the conversion rate between two currencies
    public double calculateConversionRate(String fromCurrency, String toCurrency) {
        String ultimateParentFrom = findUltimateParent(fromCurrency);
        String ultimateParentTo = findUltimateParent(toCurrency);
        if (!ultimateParentFrom.equals(ultimateParentTo)) {
            return -1; // Conversion not possible
        }
        return exchangeRate.get(fromCurrency) / exchangeRate.get(toCurrency);
    }

    public static void main(String[] args) {
        CurrencyExchange exchange = new CurrencyExchange();

        // Example exchange rates
        exchange.addCurrency("GBP", "EUR", 10);
        exchange.addCurrency("EUR", "USD", 1.1);
        exchange.addCurrency("USD", "JPY", 108.3);

        // Example queries
        System.out.println("10 GBP to USD: " + exchange.calculateConversionRate("GBP", "USD") * 10); // 10 * 1.1 = 11
        System.out.println("10 GBP to JPY: " + exchange.calculateConversionRate("GBP", "JPY") * 10); // 10 * 1.1 * 108.3 =
                                                                                                // 1191.3
    }

}
