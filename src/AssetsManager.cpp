#include "AssetsManager.hpp"

AssetsManager::AssetsManager()
{
    //ctor
}

AssetsManager& AssetsManager::getInstance()
{
        static AssetsManager _am;
        return _am;
}
std::shared_ptr<sf::Texture> AssetsManager::getTexture(std::string _path)
{

}
