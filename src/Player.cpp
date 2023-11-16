#include "Player.hpp"

Player::Player()
{
     m_sprite.setTexture( AssetsManager::getInstance().getTexture("./player.png") );
     m_position = sf::Vector2f(320,240);
     m_sprite.setPosition(m_position);
}

Player::~Player()
{
    //dtor
}
void Player::update(sf::Time _elapsedTime)
{
    if( sf::Keyboard::isKeyPressed(sf::Keyboard::W))m_position.y = m_position.y - _elapsedTime.asMilliseconds()*0.3;
    if( sf::Keyboard::isKeyPressed(sf::Keyboard::S))m_position.y = m_position.y + _elapsedTime.asMilliseconds()*0.3;

    if( sf::Keyboard::isKeyPressed(sf::Keyboard::A))m_position.x = m_position.x - _elapsedTime.asMilliseconds()*0.4;
    if( sf::Keyboard::isKeyPressed(sf::Keyboard::D))m_position.x = m_position.x + _elapsedTime.asMilliseconds()*0.4;

    m_sprite.setPosition(m_position);
}
void Player::draw(sf::RenderWindow& _window)
{
    _window.draw(m_sprite);
}

