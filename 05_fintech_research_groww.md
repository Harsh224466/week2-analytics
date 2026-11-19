# FinTech Business Understanding & Research Report

## 1. Indian Capital Market Ecosystem
* **Market Participants:** Retail investors, Domestic Institutional Investors (DIIs such as mutual funds and insurers), Foreign Portfolio Investors (FPIs), stockbrokers, exchanges (NSE/BSE), and clearing corporations.
* **SEBI (Securities and Exchange Board of India):** India's statutory market regulator responsible for protecting retail investors, enforcing compliance, and regulating brokers, mutual funds, and listed companies.
* **Brokerage Platforms:** SEBI-registered intermediaries (such as Zerodha, Groww, and Upstox) providing web and mobile interfaces that route user orders to stock exchanges.
* **Demat Accounts & Depositories (NSDL & CDSL):** A **Demat (Dematerialized) Account** holds an investor's shares electronically. **NSDL** and **CDSL** are India's two central depositories acting as electronic vaults, while brokers act as Depository Participants (DPs).
* **Trading Lifecycle & Settlement Process (`T+1`):**
  1. **Order Placement:** Investor places a buy/sell order via the broker app.
  2. **Order Routing & Matching:** Broker routes the order to NSE/BSE, where the exchange order book matches buyer and seller prices.
  3. **Clearing & Settlement:** Clearing corporations confirm funds and securities; shares credit to the buyer's Demat account and funds credit to the seller's bank account within **1 working day (`T+1`)**.

---

## 2. Case Study: How Groww Uses Data Analytics
**Groww** is one of India's largest retail investment platforms, offering stocks, direct mutual funds, IPOs, ETFs, and derivatives through a simplified mobile-first experience.

### A. Improving Customer Experience
* **Onboarding Funnel Optimization:** Data analysts track step-by-step user drop-offs across digital KYC (PAN verification, bank linking, Aadhaar e-sign) to remove friction points and reduce account activation time to minutes.
* **Personalized Discovery & Nudges:** Behavioral segmentation distinguishes first-time mutual fund investors from active equity traders, surfacing tailored educational content, SIP reminders, and risk-aligned fund collections.

### B. Driving Business & Product Decisions
* **Cross-Sell & Cohort Retention Analysis:** Tracking user cohorts over time revealed when mutual fund investors were ready to adopt stocks, IPOs, or fixed-income products—guiding product launches and boosting Customer Lifetime Value (LTV).
* **Infrastructure & Peak-Load Forecasting:** Historical order-volume analytics around major market events (Union Budget, RBI policy days, high-demand IPO listings) inform server auto-scaling so order execution stays fast and reliable during traffic spikes.