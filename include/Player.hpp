#ifndef PLAYER_HPP
#define PLAYER_HPP
#include "BasicInGameElement.hpp"

class Player final:
      public BasicInGameElement
{
    public:
        Player();
        virtual ~Player();
        virtual void update(sf::Time _elapsedTime);
        virtual void draw(sf::RenderWindow& _window);
    protected:

    private:
};

#endif // PLAYER_HPP
