PGDMP     *                    |            empleado    15.1    15.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    22468    empleado    DATABASE     }   CREATE DATABASE empleado WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Ecuador.1252';
    DROP DATABASE empleado;
                postgres    false            �            1255    22510 1   getempleado(character varying, character varying)    FUNCTION     �  CREATE FUNCTION public.getempleado(cedulaempleado character varying, nombreempleado character varying) RETURNS TABLE(id integer, cedula character varying, nombre character varying, telefono character varying, correo character varying, fecha_nacimiento date, sexo character varying, edad integer, nomdepartamento character varying, sueldo numeric, estado boolean)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY SELECT empleado."id",
					empleado."cedula",
					empleado."nombre",
					empleado."telefono",
					empleado."correo",
					empleado."fecha_nacimiento",
					empleado."sexo",
					empleado."edad",
					departamento."nombre" AS nomdepartamento,
					empleado."sueldo",
					empleado."estado"
FROM empleado
LEFT JOIN departamento ON departamento.id = empleado.id_departamento
WHERE (empleado.cedula LIKE CONCAT('%',cedulaempleado,'%')
AND empleado.nombre LIKE CONCAT('%',nombreempleado,'%'))
ORDER BY empleado.id ASC;
END;
$$;
 f   DROP FUNCTION public.getempleado(cedulaempleado character varying, nombreempleado character varying);
       public          postgres    false            �            1259    22480    departamento    TABLE     j   CREATE TABLE public.departamento (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL
);
     DROP TABLE public.departamento;
       public         heap    postgres    false            �            1259    22479    departamento_id_seq    SEQUENCE     �   ALTER TABLE public.departamento ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.departamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            �            1259    22491    empleado    TABLE     �  CREATE TABLE public.empleado (
    id integer NOT NULL,
    cedula character varying(13) NOT NULL,
    nombre character varying(255) NOT NULL,
    telefono character varying(13),
    correo character varying(150),
    fecha_nacimiento date NOT NULL,
    sexo character varying(1),
    edad integer NOT NULL,
    id_departamento integer NOT NULL,
    sueldo numeric(20,2) NOT NULL,
    estado boolean DEFAULT true NOT NULL
);
    DROP TABLE public.empleado;
       public         heap    postgres    false            �            1259    22490    empleado_id_seq    SEQUENCE     �   ALTER TABLE public.empleado ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.empleado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217                       0    22480    departamento 
   TABLE DATA           2   COPY public.departamento (id, nombre) FROM stdin;
    public          postgres    false    215   �                 0    22491    empleado 
   TABLE DATA           �   COPY public.empleado (id, cedula, nombre, telefono, correo, fecha_nacimiento, sexo, edad, id_departamento, sueldo, estado) FROM stdin;
    public          postgres    false    217   -       	           0    0    departamento_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.departamento_id_seq', 5, true);
          public          postgres    false    214            
           0    0    empleado_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.empleado_id_seq', 1, false);
          public          postgres    false    216            m           2606    22484    departamento departamento_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT departamento_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.departamento DROP CONSTRAINT departamento_pkey;
       public            postgres    false    215            o           2606    22503    empleado empleado_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT empleado_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.empleado DROP CONSTRAINT empleado_pkey;
       public            postgres    false    217            p           2606    22497    empleado fk_id_departamento    FK CONSTRAINT     �   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT fk_id_departamento FOREIGN KEY (id_departamento) REFERENCES public.departamento(id) ON UPDATE CASCADE ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.empleado DROP CONSTRAINT fk_id_departamento;
       public          postgres    false    217    215    3181                X   x��;�  й='0�w 㬫K��@Ih��2����5I�@9�,�θ@|��7r�W�����ެZ8{!��;�4n�	��            x������ � �     