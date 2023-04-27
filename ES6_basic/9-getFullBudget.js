import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    get incomeInDollars() {
      return `$${income}`;
    },
    get incomeInEuros() {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
