# Full-stack
Today, unlike other days in Full-stack, was very productive. Let me just break it down into three course contents. What we learnt today was, we learnt about positioning, we learnt about cascading, and specifity.

Cascading talks about when the position of a CSS rule matters over the rest. So in position, if a rule is defined more than once, the last to appear will be the rule that is applied to the HTML property. The bottom is considered over the first.

I'm talking about specificity. Specificity is when a rule is targeted specifically for an application. There can be certain cases when a rule can be inside the same development, can have the same class, can have the same ID. It's not possible for it to have the same ID, but to understand what I'm getting at. So, if a rule has the same class, has the same div, has the same attributes, there must be one of the same thing which the rule does not have. So that is the way we apply specificity. This specificity can be applied in different ways, which are
1. Direct descendant method
`<prop> > <prop>{}`
This is applied to the dirct descendant of the of the parent
2. I will call it generational method
`<prop> <prop>{}`
This css rule allows the css to be applied to any child of the parent container
3. Comma method
`<prop>, <prop>{}`
This allows the css to be applied to more than one property
4. Specifity method
`<prop><attribute><class><id>`
This is applying the rule to a specific property without. There should be no space between them
