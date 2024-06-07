package Questions.Graph.DisjointSetMST;


import java.util.HashMap;

public class CurrencyExchange {

    private final HashMap<String, String> parent;
    private final HashMap<String, Double> exchangeRate;

    public CurrencyExchange() {
        parent = new HashMap<>();
        exchangeRate = new HashMap<>();
    }

    // Method to update exchange rate for a currency
    public void updateCurrency(String currency, String parentCurrency, double rate, double oldRate) {
        if (!parent.containsKey(currency)) {
            return;
        }
        if (parent.get(currency).equals(parentCurrency)) {
            System.out.println("Updating exchange rate for " + currency + " to " + rate);
            exchangeRate.put(currency, (exchangeRate.get(currency) * rate) / oldRate);
        }else {
            exchangeRate.put(currency, (exchangeRate.get(currency) * rate) / exchangeRate.get(parentCurrency));
            parent.put(currency, parentCurrency);
        }
    }

    // Add a new currency with its parent and exchange rate
    public void addCurrency(String currency, String parentCurrency, double rate) {
        parent.put(currency, parentCurrency);
        exchangeRate.put(currency, rate);
        if (!exchangeRate.containsKey(parentCurrency)) {
            exchangeRate.put(parentCurrency, 1.0);
        }
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
        exchange.addCurrency("USD", "JPY", 108.3);
        exchange.addCurrency("GBP", "EUR", 10);
        exchange.addCurrency("EUR", "USD", 1.1);

        // Example queries
        System.out.println("10 GBP to USD: " + exchange.calculateConversionRate("GBP", "USD") * 10); // 10 * 1.1 = 11
        System.out.println("10 GBP to JPY: " + exchange.calculateConversionRate("GBP", "JPY") * 10); // 10 * 1.1 * 108.3 =
                                                                                                // 1191.3

        // Suppose the exchange rate for USD to JPY changes
        exchange.updateCurrency("USD", "JPY", 10, 108.3);
        System.out.println("10 GBP to JPY after update: " + exchange.calculateConversionRate("GBP", "JPY") * 10);// 10 *
                                                                                                                // 1.1 * 110
                                                                                                                // = 1210
    }

}
