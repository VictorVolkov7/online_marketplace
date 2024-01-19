import React, { useContext } from "react";
import { Link, useLocation } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import Card from "../card/Card";

function Cards({ ads }) {
  let { user } = useContext(AuthContext);
  let location = useLocation().pathname;
  return (
    <section className={`cards ${location === "/profile" ? "padding" : ""}`}>
      {!ads.length ? (
        <p>У Вас еще нет обьявлений.</p>
      ) : (
        <ul
          className={`cards__container ${
            location === "/profile"
              ? "cards__container-profile"
              : "cards__container"
          }`}
        >
          {ads.map((card) => {
            return (
              <Link
                key={card.id}
                to={user ? `ads/${card.id}` : "/"}
                className="cards__link"
              >
                <Card
                  key={card.id}
                  pk={card.id}
                  title={card.title}
                  image={card.image}
                  price={card.price}
                  description={card.description}
                />
              </Link>
            );
          })}
        </ul>
      )}
    </section>
  );
}

export default Cards;
