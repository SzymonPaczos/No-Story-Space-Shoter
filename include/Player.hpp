#ifndef PLAYER_HPP
#define PLAYER_HPP
#include "BasicInGameElement.hpp"
#include "AssetsManager.hpp"

class Player final:
      public BasicInGameElement
{
    public:
        Player();
        Player( Player & m_player ) = delete;
        Player( Player && m_player ) = delete;
        Player & operator=( Player & m_player) = delete;
        Player & operator=( Player && m_player) = delete;
        virtual ~Player();
        virtual void update(sf::Time _elapsedTime);
        virtual void draw(sf::RenderWindow& _window);
    protected:

    private:
        sf::Sprite m_sprite;
        sf::Vector2f m_position;
};

#endif // PLAYER_HPP
