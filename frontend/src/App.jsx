import { useEffect, useState } from 'react';

export default function App() {
  const [recipes, setRecipes] = useState([]);
  // useEffect(() => {
  //   fetch('/api/recipes/'), then((r) => r.json()).then(setRecipes);
  // }, []);

  return (
    <main style={{ padding: 24 }}>
      <h1>Dziala</h1>
      {/* <h1>SmakFit</h1>
      <button
        onClick={() => {
          fetch('/api/recipes/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              name: 'Owsianka',
              kcal: 420,
              protein: 18,
              fat: 10,
              carbs: 65,
              tags: ['breakfast', 'vegetarian'],
            }),
          }).then(() => location.reload());
        }}
      >
        Add recipe
      </button>
      <ul>
        {recipes.map((r) => (
          <li key={r.id}>
            {r.name} — {r.kcal} kcal
          </li>
        ))}
      </ul> */}
    </main>
  );
}
