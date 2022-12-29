#include "BasicInGameElement.hpp"

BasicInGameElement::BasicInGameElement()
{
    //ctor
}

BasicInGameElement::~BasicInGameElement()
{
    //dtor
}
inline sf::Vector2i& BasicInGameElement::getPosition()
{
    return this->m_currentPosition;
}
inline void BasicInGameElement::setPosition(sf::Vector2i& _newPosition)
{
    this->m_currentPosition = _newPosition;
}
