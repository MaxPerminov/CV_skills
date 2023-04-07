const  textfList = ["hello", "world", "nokia"];

describe('template spec', () => {
  it('passes', () => {

    cy.visit(Cypress.env())

    for (const i of textfList) {
      cy.get('[jsaction="paste:puy29d;"]').type(i)
      cy.get('[jsaction="paste:puy29d;"]').clear()
    }
    cy.get('[jsaction="paste:puy29d;"]').type("samsung")
    cy.get('[type="submit"]').first().click()
  })
})