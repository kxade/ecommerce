import pytest

from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
                            'id, name, slug, is_active',
                            [
                                (1, 'fashion', 'fashion', 1),
                                (18, 'trainers', 'trainers', 1),
                                (35, 'baseball', 'baseball', 1),
                            ],
                        )
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    print(result.name)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
                            'slug, is_active',
                            [
                                ('fashion', 1),
                                ('trainers', 1),
                                ('baseball', 1),
                            ],
                        )
def test_inventory_db_category_insert_data(
    db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active = is_active)
    print(result.name)
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
                            'id, web_id, name, slug, description, is_active, created_at, updated_at',
                            [
                                (   
                                    1,
                                    "45425810",
                                    'windstar running sneakers',
                                    "windstar-running-sneakers",
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                    1,
                                    "2022-11-22 12:44",
                                    "2022-11-22 12:44",        
                                ),
                                (   
                                    8616,
                                    "45425810",
                                    'impact puse dance shoe',
                                    "impact-puse-dance-shoe",
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                    1,
                                    "2022-11-22 12:44",
                                    "2022-11-22 12:44",        
                                ),
                            ],  
                        )
def test_inventory_product_dbfixture(
                                        db, 
                                        db_fixture_setup, id, 
                                        web_id, 
                                        name, 
                                        slug, 
                                        description, 
                                        is_active, 
                                        created_at, 
                                        updated_at
                                    ):
    result = models.Product.objects.get(id=id)
    result_create_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    
    print(result.name)
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result.created_at == created_at
    assert result.updated_at == updated_at


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
    db, product_factory, category_factory, slug, is_active
):
    new_categoty = category_factory.create()
    new_product = product_factory.create(category=(1, 36))
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 2

    
