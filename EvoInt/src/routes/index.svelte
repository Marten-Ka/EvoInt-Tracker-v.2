<script lang="ts">
	import { goto } from '$app/navigation';
	import Saos from 'saos';
	import RedirectButton from '../components/RedirectButton.svelte';
	import Header from '../components/Header.svelte';
	import Icon from '../components/Icon.svelte';
	import InformationTile from '../components/InformationTile.svelte';
	import AnimationContainer from '../components/AnimationContainer.svelte';
	import Footer from '../components/Footer.svelte';
	import ArticleCard from '../components/ArticleCard.svelte';

	let show: boolean = false;

	function onClick() {
		show = !show;
	}

	function navHelp() {
		goto('/help');
	}

</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="headline text-center text-base  sm:text- md:text-xl lg:text-3xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none"
	>
		Entdecke die Evolution <br /> von künstlicher Intelligenz
	</h1>
	<h2
		class="mt-2 mb-20 text-center text-sm  sm:text-base md:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl font-semibold text-gray-400 uppercase"
	>
		Wir nehmen dich mit auf eine Reise durch die Geschichte
	</h2>
	<div class="arrow">
		<Icon
			icon="chevron-down"
			fill_color="none"
			color="#111827CC"
			size="192px"
			class="hover:cursor-pointer hover:scale-105 transition-all duration-500 hover:translate-y-4"
			onClick={() => {
				goto('#page-content');
			}}
		/>
	</div>
</div>

<div class="wave-1">
	<svg
		data-name="Layer 1"
		xmlns="http://www.w3.org/2000/svg"
		viewBox="0 0 1200 120"
		preserveAspectRatio="none"
	>
		<path
			d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
			opacity=".25"
			class="shape-fill"
		/>
		<path
			d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
			opacity=".5"
			class="shape-fill"
		/>
		<path
			d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
			class="shape-fill"
		/>
	</svg>
</div>

<div class="background-lightning" />

<div id="page-content" class="section xl:p-12">
	<InformationTile
		title="Vikus Viewer"
		content="Erlebe historische Daten auf einem Blick. Erkenne Verläufe, beobachte Trends und untersuche Änderungen."
		class="mt-10 lg:mt-20"
	>
		<div slot="left_slot" class="mt-2 flex justify-center  gap-5">
			<Icon icon="bar-chart-2" size="32px" />
			<Icon icon="trending-up" size="32px" />
			<Icon icon="search" size="32px" />
		</div>
		<div slot="right_slot">
			<AnimationContainer from_right>
				<img
					src="../static/vikusViewer.png"
					alt="vikus_viewer"
					class="rounded-3xl shadow-2xl px-4"
				/>
			</AnimationContainer>
		</div>
	</InformationTile>
	<InformationTile title="Zusammenhänge schaffen" right_side class="mt-10 lg:mt-20">
		<div
			slot="content"
			class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-center lg:text-justify"
		>
			Daten ohne Kontext bringen meist keinen Nutzen. Dadurch haben wir es uns zur Aufgabe gemacht
			einen Zusammenhang zwischen den großen Datenmengen zu schaffen. <br /> Durch NLP
			<span class="font-mono text-xl">(Natural Language Processing)</span> analysieren wir verschiedenste
			Trends in der Geschichte.
		</div>
		<div slot="left_slot" class="mt-2 flex flex-row-reverse justify-center gap-5">
			<Icon icon="list" size="32px" />
			<Icon icon="layers" size="32px" />
			<Icon icon="database" size="32px" />
		</div>
		<div slot="right_slot">
			<AnimationContainer>
				<img src="../static/NLP.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl px-4" />
			</AnimationContainer>
		</div>
	</InformationTile>

	<section class="my-32 p-4 md:p-12 text-gray-800 text-center w-[95%] bg-gray-800 rounded-xl">
		<h2
			class="text-center text-base  md:text-xl lg:text-3xl xl:text-4xl uppercase text-gray-100 font-bold mb-12 pb-4"
		>
			Neueste Artikel
		</h2>

		<div class="grid lg:grid-cols-3 gap-6 xl:gap-x-12">
			<ArticleCard
				img_source="../../static/homeml.jpg"
				img_height="h-72"
				img_alt="ML"
				reference="/tutorial/ml"
				source_link="https://cdn.futura-sciences.com/buildsv6/images/wide1920/9/0/b/90b0048886_50162050_machine-learning1.jpg"
				source_text="Quelle: Futura Science"
				heading="Machine Learning"
				publication_date="01.06.2022"
				author="Hamid Omar"
				content="Erfahre mehr rund um das Thema Machine Learning und wie es mit Künstlichen
				Intelligenzen zusammenhängt."
			/>

			<ArticleCard
				img_source="../../static/homeki.jpg"
				img_height="h-96"
				img_alt="KI"
				reference="/tutorial/ki"
				source_link="https://www.planet-wissen.de/sendungen/kuenstliche-intelligenz-roboter-104~_v-gseagaleriexl.jpg"
				source_text="Quelle: Planet Wissen"
				heading="Künstliche Intelligenz"
				publication_date="25.07.2022"
				author="Robert Witzke"
				content="Erfahre mehr rund um das Thema Künstliche Intelligenz - von der Begriffsklärung über
				die Historie bis hin zu den Arten von KI."
			/>

			<ArticleCard
				img_source="../../static/homenlp.jpeg"
				img_height="h-72"
				img_alt="NLP"
				reference="/tutorial/nlp"
				source_link="https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters:format(jpg)/https:%2F%2Fblogs-images.forbes.com%2Fbernardmarr%2Ffiles%2F2019%2F06%2F5-Amazing-Examples-Of-Natural-Language-Processing-NLP-In-Practice-1200x639.jpeg"
				source_text="Quelle: Forbes"
				heading="Natural Language Processing"
				publication_date="01.08.2022"
				author="Marten Kaffler"
				content="Erfahre mehr rund um das Thema Natural Language Processing und wie Computer unsere
				natürliche Sprache verstehen und verarbeiten können."
			/>
		</div>
	</section>

	<Footer />
</div>

<style lang="postcss">
	.background-lightning {
		@apply absolute top-full w-full shadow-white shadow-2xl z-50;
		box-shadow: 0px 0px 180px 10px #fff;
	}

	.arrow {
		@apply bg-transparent;
	}

	.wave-1 {
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		overflow: hidden;
		line-height: 0;
		transform: rotate(180deg);
	}

	.wave-1 svg {
		position: relative;
		display: block;
		width: calc(100% + 1.3px);
		height: 150px;
	}

	.wave-1 .shape-fill {
		fill: #111827;
	}

	.section {
		@apply absolute top-full w-full flex flex-col gap-y-24 items-center bg-gray-900;
	}

	@keyframes -global-from-left {
		0% {
			transform: translateX(-10vw);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}
</style>
